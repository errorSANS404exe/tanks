import wrap
import wrap as UwU, time
from wrap import world, sprite, actions

world.create_world(1000, 1000)
dragon = sprite.add("mario-enemies", 300, 200, "dragon_stand1")
tank = sprite.add("battle_city_tanks", 100, 300, "tank_enemy_size3_green2")
tree = sprite.add("mario-scenery", 400, 500, "tree_large")


@wrap.on_mouse_down(wrap.BUTTON_WHEELUP, wrap.BUTTON_WHEELDOWN)
def resizing(pos_x, pos_y, button):
    point = sprite.is_collide_point(dragon, pos_x, pos_y)
    if wrap.BUTTON_WHEELUP == button and point:
        sprite.set_size(dragon, sprite.get_width(dragon) + 15, sprite.get_height(dragon) + 15)
    if wrap.BUTTON_WHEELDOWN == button and point:
        sprite.set_size(dragon, sprite.get_width(dragon) - 15, sprite.get_height(dragon) - 15)

    point = sprite.is_collide_point(tank, pos_x, pos_y)
    if wrap.BUTTON_WHEELUP == button and point:
        sprite.set_size(tank, sprite.get_width(tank) + 15, sprite.get_height(tank) + 15)
    if wrap.BUTTON_WHEELDOWN == button and point:
        sprite.set_size(tank, sprite.get_width(tank) - 15, sprite.get_height(tank) - 15)

    point = sprite.is_collide_point(tree, pos_x, pos_y)
    if wrap.BUTTON_WHEELUP == button and point:
        sprite.set_width_proportionally(tree, sprite.get_width(tree) + 15)
    if wrap.BUTTON_WHEELDOWN == button and point:
        sprite.set_height_proportionally(tree, sprite.get_height(tree) - 15)
