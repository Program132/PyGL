import glm
import pygame as pg

FOV = 50  # degrée
NEAR = 0.1
FAR = 100


class Camera:
    def __init__(self, app):
        self.app = app
        self.aspect_ratio = app.WIN_SIZE[0] / app.WIN_SIZE[1]
        # on met la position de la camera : (position + up)
        self.position = glm.vec3(2, 3, 3)
        self.up = glm.vec3(0, 1, 0)
        self.m_proj = self.get_projection_matrix()
        # pour avoir la vue de la matrice on devra utiliser glm
        self.m_view = self.get_view_matrix()

    def get_projection_matrix(self):
        return glm.perspective(glm.radians(FOV), self.aspect_ratio, NEAR, FAR)

    def get_view_matrix(self):
        """
        lookAt(eye, center, up)

        eye : position de la camera
        center : position où la camera doit regarder
        up : comment la camera est orienté
        """
        return glm.lookAt(self.position, glm.vec3(0), self.up)