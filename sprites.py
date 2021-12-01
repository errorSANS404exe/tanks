import wrap
import wrap as UwU, time
from wrap import world, sprite, actions

world.create_world(1000, 1000)
dragon = sprite.add("mario-enemies", 100, 200, "dragon_stand1")
tank = sprite.add("battle_city_tanks", 400, 300, "tank_enemy_size3_green2")
tree = sprite.add("mario-scenery", 200, 500, "tree_large")


@wrap.on_mouse_down(wrap.BUTTON_WHEELUP, wrap.BUTTON_WHEELDOWN)
def resizing(pos_x, pos_y, button):
    if sprite.is_collide_point(tree, pos_x, pos_y):
        resize(button, tree)

    elif sprite.is_collide_point(tank, pos_x, pos_y):
        resize(button, tank)

    elif sprite.is_collide_point(dragon, pos_x, pos_y):
        resize(button, dragon)


def resize(button, s):
    if wrap.BUTTON_WHEELUP == button:
        sprite.set_height_proportionally(s, sprite.get_height(s) + 15)
    else:
        sprite.set_height_proportionally(s, sprite.get_height(s) - 15)


@wrap.on_key_always(wrap.K_RIGHT, wrap.K_LEFT, wrap.K_UP, wrap.K_DOWN)
def move_angle(keys, pos_x, pos_y):
    if sprite.is_collide_point(tree, pos_x, pos_y):
        move_angle2(keys, tree)

    elif sprite.is_collide_point(tank, pos_x, pos_y):
        move_angle2(keys, tank)

    elif sprite.is_collide_point(dragon, pos_x, pos_y):
        move_angle2(keys, dragon)


def move_angle2(keys, v):
    if wrap.K_RIGHT in keys:
        sprite.set_angle(v, sprite.get_angle(v) + 5)

    elif wrap.K_LEFT in keys:
        sprite.set_angle(v, sprite.get_angle(v) - 5)

    elif wrap.K_DOWN in keys:
        sprite.set_costume_next(v)

    elif wrap.K_UP in keys:
        sprite.set_costume_prev(v)
