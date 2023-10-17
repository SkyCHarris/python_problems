# The packaging system is running wild! The candy is lying loose all over the warehouse, cereal missing, bread in a bottle...
# The candy should be in plastic and the bread should be in a bag
# The packaging machine is runnign the get_container() function to retrieve the container of a product, but something isn't right

def get_container(product):
	matches = {
	"Bread" : "bag",
	"Milk" : "bottle",
	"Beer" : "bottle",
	"Eggs" : "carton",
	"Cerials" : "box",
	"Candy" : "plastic",
	"Cheese" : None
	}
	return matches[product]

get_container("Bread")
get_container("Beer")
get_container("Candy")
get_container("Cheese")