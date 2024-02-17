import numpy as np


class Triangle:
    def __init__(self, app):
        self.app = app
        self.ctx = app.ctx
        self.vbo = self.get_vbo()
        self.shader_program = self.get_shader_program("default")
        self.vao = self.get_vao()

    def get_vertex_data(self):
        """
        Renvoit les données du vertex shader, ici les points et leur positions
        """
        data = [
            (-0.6, -0.8, 0.0),
            (0.6, -0.8, 0.0),
            (0.0, 0.8, 0.0)
        ]
        data = np.array(data, dtype='f4')
        return data

    def get_vbo(self):  # Vertex Buffer Object
        """
        Renvoit le Vertex Buffer Oject depuis nos vertices (notre vertex data donné dans la fonction du dessus)
        """
        vertex_data = self.get_vertex_data()
        vbo = self.ctx.buffer(vertex_data)
        return vbo

    def get_shader_program(self, shader_name):
        """
        Charge les programmes des shaders pour les liers au VBO par la suite
        """

        with open(f'shaders/{shader_name}.frag') as f:
            fragment = f.read()

        with open(f'shaders/{shader_name}.vert') as f:
            vertex = f.read()

        program = self.ctx.program(vertex_shader=vertex, fragment_shader=fragment)
        return program

    def get_vao(self):
        """
        Renvoit le Vertex Array Object qui va unir le VBO et les Shader Program
        """
        vao = self.ctx.vertex_array(self.shader_program, [(self.vbo, '3f', 'in_position')])
        return vao

    def render(self):
        """
        Rendu du triangle
        """
        self.vao.render()

    def destroy(self):
        """
        Supprime l'objet en partant du vbo, puis les programmes et enfin le VAO
        """
        self.vbo.release()
        self.shader_program.release()
        self.vao.release()
