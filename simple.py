import wrap
import wrap as UwU, time
from wrap import world, sprite, actions

world.create_world(1000, 1000)
id = sprite.add("pacman", 200, 300, "player2")


@wrap.on_key_always(wrap.K_RIGHT, wrap.K_LEFT,wrap.K_UP)
def move5(keys):
    print(keys)
    if wrap.K_RIGHT in keys:
        angle = sprite.get_angle(id)
        sprite.set_angle(id, angle + 5)
    if wrap.K_LEFT in keys:
        angle = sprite.get_angle(id)
        sprite.set_angle(id, angle - 5)
    if wrap.K_UP in keys:
        sprite.move_at_angle_dir(id,9)