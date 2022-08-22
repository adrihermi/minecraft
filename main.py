from ursina import *
from ursina.prefabs.\
    first_person_controller \
    import FirstPersonController

from ursina.shaders import\
    lit_with_shadows_shader

app = Ursina(borderless=False)
random.seed(0)
Entity.default_shader = \
    lit_with_shadows_shader
window.size = (400, 700)

ground = Entity(
    model='plane',
    collider='box',
    scale=64,
    color=color.red
)

player = FirstPersonController()
player.position = Vec3(0, 2, 0)


class Cubo(Entity):
    def __init__(self,
                 position=(0, 0, 0)):
        super().__init__(
            position=position,
            model='cube',
            scale=(1, 1),
            origin_y=.5,
            color=color.light_gray,
            collider='box',
        )


Cubo(position=(0, 1, 0))

for z in range(30):
    Cubo(position=(random.randint(1, 5), 1, z))


def update():
    if player.position.y <= -2:
        player.position.y = Vec3(0, 10, 0)


ground.position = Vec3(0, -3, 0)
Sky()
app.run()
