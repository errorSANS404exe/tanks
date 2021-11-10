import wrap
import wrap as UwU, time
from wrap import world, sprite, actions

world.create_world(1000, 1000)
id = sprite.add("pacman", 200, 300, "player2")
phantom = sprite.add("pacman", 440, 300, "enemy_ill_white1", False)


@wrap.on_key_always(wrap.K_RIGHT, wrap.K_LEFT, wrap.K_UP)
def move5(keys):
    print(keys)
    if wrap.K_RIGHT in keys:
        angle = sprite.get_angle(id)
        sprite.set_angle(id, angle + 5)
    if wrap.K_LEFT in keys:
        angle = sprite.get_angle(id)
        sprite.set_angle(id, angle - 5)
    if wrap.K_UP in keys:
        sprite.move_at_angle_dir(id, 9)


@wrap.on_mouse_move()
def mouse_move(pos_x, pos_y, mouse_buttons):
    sprite.move_to(phantom, pos_x, pos_y)
    if wrap.BUTTON_LEFT in mouse_buttons:
        sprite.show(phantom)
    else:
        sprite.hide(phantom)


@wrap.on_mouse_down(wrap.BUTTON_LEFT)
def mouse_down():
    sprite.show(phantom)


@wrap.on_mouse_up(wrap.BUTTON_LEFT)
def mouse_up():
    sprite.hide(phantom)
