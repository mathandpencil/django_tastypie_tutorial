

EXAMPLE.MODELS.UserModel = Backbone.Model.extend({
  
	initialize: function() {
	},
	
	urlRoot : function(){
    	return '/api/v1/user/';
	},
	
});


var Users = Backbone.Collection.extend({

	model: EXAMPLE.MODELS.UserModel,
	
	url : '/api/v1/user/',
	
});

EXAMPLE.COLLECTIONS.Users = new Users;