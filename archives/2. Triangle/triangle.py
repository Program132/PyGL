import numpy as np


# OpenGL Rendering :
# On fournit des vertices, des points pour résumer, ce qui va former un "Vertex Shader"
# On assemble la forme avec nos 3 points ce qui donne un "Primitive Assembly", ce qui ressemble à un triangle avec des côtés, on connecte les points entre eux.
# Ensuite on a la "Rasterization", qui va former des "Fragments"
# Puis on a le fragment shader qui est déterminer avec des TESTS.
# Cela va être envoyé vers le "FrameBuffer"
# Enfin, pour avoir le résultat voulu le vertexshader et le fragmentshader vont s'unir pour avoir des "Uniforms Variables"


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
            #  x    y     z
            (-0.6, -0.8, 0.0),  # bas gauche
            (0.6, -0.8, 0.0),  # en haut
            (0.0, 0.8, 0.0)  # bas droit
        ]
        # Ici on le fait en 2D, voilà pourquoi en Z on a 0.0
        data = np.array(data, dtype='f4')  # on peut mettre 'f4' à la place de 'np.float32'
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

        # '#version 330 core' indique que le code est écrit selon la version 330 du langage GLSL.
        # 'layout (location = 0) out vec4 fragColor;' spécifie que la sortie de ce shader est une couleur RGBA (rouge, vert, bleu, alpha), qui sera utilisée comme couleur du fragment final.
        # 'main()' est la fonction principale du shader de fragment, qui calcule la couleur du fragment. Dans ce cas, elle définit une couleur rouge (1,0,0) et l'assigne à fragColor.

        with open(f'shaders/{shader_name}.vert') as f:
            vertex = f.read()

        # '#version 330 core' indique la version du langage GLSL utilisée.
        # 'layout (location = 0) in vec3 in_position;' spécifie que l'entrée de ce shader est une position à trois dimensions.
        # 'main()' est la fonction principale du shader de vertex, qui transforme les coordonnées du sommet en coordonnées de l'écran en utilisant la matrice de projection.
        # 'gl_Position = vec4(in_position, 1.0);' assigne les coordonnées du sommet transformées à la variable prédéfinie gl_Position, qui est utilisée pour déterminer la position du sommet à l'écran.

        program = self.ctx.program(vertex_shader=vertex, fragment_shader=fragment)
        return program

    def get_vao(self):
        """
        Renvoit le Vertex Array Object qui va unir le VBO et les Shader Program
        """
        vao = self.ctx.vertex_array(self.shader_program, [(self.vbo, '3f', 'in_position')])
        # 3f est le format du buffer
        # in_position est l'attribut -> x1,y1,z1
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
