import wrap as UwU, time
from wrap import world, sprite, actions

world.create_world(400, 600)
tank1 = sprite.add("battle_city_tanks", 100, 200, "tank_enemy_size2_purple1", False)
tank2 = sprite.add("battle_city_tanks", 300, 500, "tank_enemy_size2_white1", False)


def spawn(tank_id):
    i = sprite.add("battle_city_items", sprite.get_x(tank_id), sprite.get_y(tank_id), "effect_appearance1")
    time.sleep(0.3)
    sprite.set_costume(i, "effect_appearance2")
    time.sleep(0.3)
    sprite.set_costume(i, "effect_appearance3")
    time.sleep(0.3)
    sprite.set_costume(i, "effect_appearance4")
    time.sleep(0.3)
    sprite.set_costume(i, "effect_appearance3")
    time.sleep(0.3)
    sprite.set_costume(i, "effect_appearance2")
    time.sleep(0.3)
    sprite.set_costume(i, "effect_appearance3")
    time.sleep(0.3)
    sprite.set_costume(i, "effect_appearance4")
    sprite.remove(i)
    sprite.show(tank_id)


def explosion(tank_id):
    sprite.hide(tank_id)
    e = sprite.add("battle_city_items", sprite.get_x(tank_id), sprite.get_y(tank_id), "effect_explosion1")
    time.sleep(0.3)
    sprite.set_costume(e, "effect_explosion2")
    time.sleep(0.3)
    sprite.set_costume(e, "effect_explosion3")
    time.sleep(0.3)
    sprite.set_costume(e, "effect_explosion2")
    time.sleep(0.3)
    sprite.set_costume(e, "effect_explosion1")
    time.sleep(0.3)
    sprite.remove(e)


def move_x(tank_id, distance_x):
    if distance_x < 0:
        sprite.set_angle(tank_id, -90)
    else:
        sprite.set_angle(tank_id, 90)
    actions.move(tank_id, distance_x, 0)


def move_y(tank_id, distance_y):
    if distance_y < 0:
        sprite.set_angle(tank_id, 0)
    else:
        sprite.set_angle(tank_id, 180)
    actions.move(tank_id, 0, distance_y)


spawn(tank1)
spawn(tank2)
move_x(tank1, 100)
move_x(tank2, -150)
move_y(tank1, 100)
move_y(tank2, -200)
explosion(tank1)
explosion(tank2)
