angular.module('throne').controller('MainUiController', ['$scope', 'BathroomService', 'BathroomModel', '$interval',
function($scope, BathroomService, BathroomModel, $interval) {
    var pollBathrooms = function() {
        BathroomService.getAllBathrooms()
            .then(function(data) {
                $scope.bathrooms = data.data.map(function(bathroomData) {return new BathroomModel(bathroomData)});
            });
    };

    pollBathrooms();
    $interval(pollBathrooms, 3000);
}]);