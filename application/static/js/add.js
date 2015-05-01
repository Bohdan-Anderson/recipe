ko.bindingHandlers.uniqueId = {
	init: function(element, valueAccessor) {
		var value = valueAccessor();
		var name = element.getAttribute("name");
		if (ko.bindingHandlers.uniqueId.counter[name] != undefined) {
			var number = ++ko.bindingHandlers.uniqueId.counter[name];
		} else {
			ko.bindingHandlers.uniqueId.counter[name] = 0;
			var number = 0;
		}

		element.setAttribute("name", (name) + "_" + (number));
	},
	counter: {},
	prefix: "unique"
};

var RecipeModel = function(recipe) {
	var self = this;

	if (data.title) {
		self.title = ko.observable(data.title);
	}
	if (data.note) {
		self.note = ko.observable(data.note)
	}

	if (data.ingredient) {
		self.ingredient = ko.observableArray(ko.utils.arrayMap(data.ingredient, function(data) {
			return {
				name: data.name,
				ammount: data.ammount,
				messured: data.messured
			}
		}));
	} else {
		self.ingredient = ko.observableArray();
	};

	if (data.steps) {
		self.steps = ko.observableArray(ko.utils.arrayMap(data.steps, function(data) {
			return {
				note: data.note,
				order: data.order
			}
		}));
	} else {
		self.steps = ko.observableArray();
	};



	self.addIngredient = function() {
		self.ingredient.push({
			name: "",
			ammount: "",
			messured: ""
		});
		var last = $(".ingrident_name");
		last = last[last.length - 1];
		$(last).select();
	};

	self.removeIngredient = function(ingredient) {
		self.ingredient.remove(ingredient);
	};

	self.addStep = function() {
		self.steps.push({
			note: "",
			order: ""
		})
	}

	self.removeStep = function(step) {
		self.steps.remove(step);
	};

	self.ingredients = ko.computed(function() {
		var list = self.ingredient(),
			a = 0,
			max = list.length,
			out = "";
		for (a = 0; a < max; ++a) {
			out += list[a].ammount + " " + list[a].messured + " " + list[a].name + "\n";
		}
		return out;
	}, self);

	self.allsteps = ko.computed(function() {
		var list = self.steps(),
			a = 0,
			max = list.length,
			out = "";
		for (a = 0; a < max; ++a) {
			out += list[a].order + ". " + list[a].note + "\n";
		}
		return out;
	}, self)

	// self.save = function() {
	// 	self.lastSavedJson(JSON.stringify(ko.toJS(self.contacts), null, 2));
	// };

	// self.lastSavedJson = ko.observable("")
};

ko.applyBindings(new RecipeModel());