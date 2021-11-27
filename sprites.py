import wrap
import wrap as UwU, time
from wrap import world, sprite, actions

world.create_world(1000, 1000)
dragon = sprite.add("mario-enemies", 300, 200, "dragon_stand1")
tank = sprite.add("battle_city_tanks", 300, 200, "tank_enemy_size3_green2")
tree = sprite.add("mario-scenery", 300, 200, "tree_large")


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
