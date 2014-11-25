angular.module('throne').directive('phoneNumber', [function() {
    return {
        restrict: 'A',
        require: 'ngModel',
        link: function(scope, element, attrs, ctrl) {
            function isValidPhoneNumber(number) {
                if (!number) return false;
                return number.replace(/[^\d]/g, '').length === 10;
            };

            function parsePhoneNumber(input) {
                return input.replace(/[^\d]/g, '');
            };

            ctrl.$parsers.push(parsePhoneNumber);
            ctrl.$validators['phone'] = isValidPhoneNumber;
        }
    };
}]);