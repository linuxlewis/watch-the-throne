angular.module('BathroomsMod')
.factory('BathroomService', ['$http', function($http) {
    var getAllBathrooms = function() {
        return $http.get('/bathrooms');
    };

    return {
        getAllBathrooms: getAllBathrooms
    };
}]);
