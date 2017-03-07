from family import Person

p = Person(1, "Julien", [02, 29, 1900], "Male", "Blue")
p.last_name = "Dupont"
print "New person %s %s" % (p.get_first_name(), p.last_name)
