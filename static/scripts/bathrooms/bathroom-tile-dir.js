angular.module('BathroomsMod')
.directive('bathroomTile', ['$http', function($http) {
    return {
        restrict: 'E',
        templateUrl: '/static/templates/bathroom-tile-dir.html',
        replace: true,
        link: function(scope) {
            scope.submitPhoneNumber = function() {
                scope.successMessage = '';
                scope.errorMessage = '';
                if (scope.phoneForm.$valid) {
                    scope.loading = true;

                    var params = {
                        bathroom: scope.bathroom.id,
                        number: scope.phoneNumber
                    };

                    $http.post('/bathroomalerts/', params)
                        .then(function() {
                            scope.loading = false;
                        })
                        .then(function(data) {
                            scope.successMessage = "You will receive a text when the throne is available.";
                        }, function(data) {
                            scope.errorMessage = "Your number did not save successfully";
                        });
                } else {
                    scope.errorMessage = "Please enter a valid 10-digit phone number";
                }
            };

            scope.$watch('bathroom.available', function() {
                scope.errorMessage = null;
                scope.successMessage = null;
            });
        }
    };
}]);