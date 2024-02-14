import pygame as pg
import moderngl as mgl
import sys


class GraphicsEngine:
    def __init__(self, winSize=(1600, 900)):
        # initialisation de pygame
        pg.init()
        # Taille de la fenêtre
        self.WIN_SIZE = winSize  # weight, height OU x, y
        # Versions OpenGL
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)  # version majeur
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)  # version mineur
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK,
                                    pg.GL_CONTEXT_PROFILE_CORE)  # On met le "profile mask" à "profile core" pour ne pas avoir des fonctionnalités "deprecated"
        # Création du context pour opengl
        pg.display.set_mode(self.WIN_SIZE, flags=pg.OPENGL | pg.DOUBLEBUF)
        # Doublebuf : Le double buffering fournit 2 buffers de couleur utiliser dans le dessin.
        # Un buffer est affiché tant que l'autre est entrain de dessiner.
        # Quand le dessin est fini, les 2 buffers sont échangé pour que celui qui était visualisé soit maintenant utilisé pour dessiner.
        # Plus d'infos siur les buffers : https://stackoverflow.com/questions/12887802/what-exactly-is-a-buffer-in-opengl-and-how-can-i-use-multiple-ones-to-my-advant
        # Detection et utilisation de notre context
        self.ctx = mgl.create_context()
        # Clock classe pour les frame rats et delta time
        self.clock = pg.time.Clock()

    def check_events(self):
        """
        Fonction pour analyser les évènements de l'utilisateur
        """
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
                # On vérifie si c'est la croix ou échap.

    def render(self):
        """
        Fonction de rendu
        """
        # Suppresion des framebuffers pour préparers l'écran et delete les données d'avant, afin d'éviter le mélange d'informations indésirables
        self.ctx.clear(color=(0.08, 0.16, 0.17))
        # Mettre à jour les buffers (échange les buffers)
        pg.display.flip()

    def run(self):
        while True:
            self.check_events()
            self.render()
            self.clock.tick(60)


if __name__ == "__main__":
    app = GraphicsEngine()
    app.run()