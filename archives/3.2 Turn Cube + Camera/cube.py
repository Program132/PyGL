import numpy as np
import glm


class Cube:
    def __init__(self, app):
        self.app = app
        self.ctx = app.ctx
        self.vbo = self.get_vbo()
        self.shader_program = self.get_shader_program("default")
        self.vao = self.get_vao()
        self.m_model = self.get_model_matrix()
        self.on_init()

    def get_vertex_data(self):
        """
        Renvoit les données du vertex shader, ici les points et leur positions
        """
        vertices = [
            (-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1),
            (-1, 1, -1), (-1, -1, -1), (1, -1, -1), (1, 1, -1)
        ]

        indices = [
            (0, 2, 3), (0, 1, 2),
            (1, 7, 2), (1, 6, 7),
            (6, 5, 4), (4, 7, 6),
            (3, 4, 5), (3, 5, 0),
            (3, 7, 4), (3, 2, 7),
            (0, 6, 1), (0, 5, 6)
        ]

        vertex_data = self.get_data(vertices, indices)
        return vertex_data

    @staticmethod
    def get_data(vertices, indices):
        data = [vertices[ind] for triangle in indices for ind in triangle]
        return np.array(data, dtype='f4')

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

    def update(self):
        m_model = glm.rotate(self.m_model, self.app.time, glm.vec3(0, 1, 0))
        self.shader_program["m_model"].write(m_model)

    def render(self):
        """
        Rendu du cube
        """
        self.update()
        self.vao.render()

    def destroy(self):
        """
        Supprime l'objet en partant du vbo, puis les programmes et enfin le VAO
        """
        self.vbo.release()
        self.shader_program.release()
        self.vao.release()

    def get_model_matrix(self):
        """
        Renvoie la matrix d'identité 4
        """
        m_model = glm.mat4()
        return m_model

    def on_init(self):
        """
        Passe la projection de la camera vers le shader
        """
        self.shader_program['m_proj'].write(self.app.camera.m_proj)
        self.shader_program['m_view'].write(self.app.camera.m_view)
        self.shader_program['m_model'].write(self.m_model)
