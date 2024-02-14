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
        data = np.array(data, dtype=np.float32)  # on peut mettre 'f4' à la place de 'np.float32'
        return data

    def get_vbo(self):  # Vertex Buffer Object
        """
        Renvoit le VBO pour avoir notre shader
        :return:
        """
        vertex_data = self.get_vertex_data()
        vbo = self.ctx.buffer(vertex_data)
        return vbo
