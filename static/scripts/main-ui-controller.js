angular.module('throne').controller('MainUiController', ['$scope', 'BathroomService', 'BathroomModel', '$timeout',
function($scope, BathroomService, BathroomModel, $timeout) {
    var pollBathrooms = function() {
        BathroomService.getAllBathrooms()
            .then(function(data) {
                $scope.bathrooms = data.data.map(function(bathroomData) {return new BathroomModel(bathroomData)});
            });
    };

    pollBathrooms();
    // $timeout(pollBathrooms, 5000);
}]);