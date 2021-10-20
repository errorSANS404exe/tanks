import wrap as UwU, time
from wrap import world, sprite

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


spawn(tank1)
spawn(tank2)
