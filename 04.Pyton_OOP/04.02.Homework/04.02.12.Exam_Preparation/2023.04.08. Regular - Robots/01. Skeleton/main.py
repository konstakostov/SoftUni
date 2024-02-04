from project.robots_managing_app import RobotsManagingApp

main_app = RobotsManagingApp()

print()

print(main_app.add_service('SecondaryService', 'ServiceRobotsWorld'))
print(main_app.add_service('MainService', 'ServiceTechnicalsWorld'))

print()

print(main_app.add_robot('FemaleRobot', 'Scrap', 'HouseholdRobots', 321.26))
print(main_app.add_robot('FemaleRobot', 'Sparkle', 'FunnyRobots', 211.11))

print()

print(main_app.add_robot_to_service('Scrap', 'ServiceRobotsWorld'))
print(main_app.add_robot_to_service('Sparkle', 'ServiceRobotsWorld'))

print()

print(main_app.feed_all_robots_from_service('ServiceRobotsWorld'))
print(main_app.feed_all_robots_from_service('ServiceTechnicalsWorld'))

print()

print(main_app.service_price('ServiceRobotsWorld'))
print(main_app.service_price('ServiceTechnicalsWorld'))

print()

print(str(main_app))

print()

print(main_app.remove_robot_from_service('Scrap', 'ServiceRobotsWorld'))

print(main_app.service_price('ServiceRobotsWorld'))
print(main_app.service_price('ServiceTechnicalsWorld'))

print()

print(str(main_app))


# SecondaryService is successfully added.
# MainService is successfully added.
#
# FemaleRobot is successfully added.
# FemaleRobot is successfully added.
#
# Successfully added Scrap to ServiceRobotsWorld.
# Successfully added Sparkle to ServiceRobotsWorld.
#
# Robots fed: 2.
# Robots fed: 0.
#
# The value of service ServiceRobotsWorld is 532.37.
# The value of service ServiceTechnicalsWorld is 0.00.
#
# ServiceRobotsWorld Secondary Service:
# Robots: Scrap Sparkle
# ServiceTechnicalsWorld Main Service:
# Robots: none
# Successfully removed Scrap from ServiceRobotsWorld.
# The value of service ServiceRobotsWorld is 211.11.
# The value of service ServiceTechnicalsWorld is 0.00.
# ServiceRobotsWorld Secondary Service:
# Robots: Sparkle
# ServiceTechnicalsWorld Main Service:
# Robots: none
