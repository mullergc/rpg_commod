import class_test

gov = class_test.Government(100)
hosp = class_test.Hospital(3)
media = class_test.Media()

# Government distributes resources
resources_to_distribute = 50
resources_distributed = gov.distribute_resources(resources_to_distribute)


# Hospital receives resources
resources_received = hosp.receive_resources(resources_distributed)
