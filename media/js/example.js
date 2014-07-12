EXAMPLE.VIEWS.ExampleListItem = Backbone.View.extend({ 
	
	tagName : 'div',

	initialize : function(model, options){
		this.options = options
	},

	events : {
	},

	template : _.template("<div>username: <%- username %> email: <%- email %> id: <%- id  %></div>"),
	

	render : function() {
		this.$el.html(this.template(this.model.toJSON()));
		return this;
	}
});


EXAMPLE.VIEWS.ExampleList = Backbone.View.extend({ 
	
	el : "#my-model-list",
  
	
	initialize : function(options){
		this.listenTo(EXAMPLE.COLLECTIONS.Users, 'reset', this.addAll, this);
	},
	
	addOne : function(model) {
		var view = new EXAMPLE.VIEWS.ExampleListItem ({ model : model })
		console.log( view.render().el )
		this.$el.append(view.render().el)
	},
	
	addAll : function(){    
		var that = this;
		EXAMPLE.COLLECTIONS.Users.each(function(model){
			that.addOne(model);
		});
	},
  
	render : function() {
		this.$el.html(this.template());
		return this;
	}
	
});