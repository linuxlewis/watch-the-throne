angular.module('BathroomsMod', []);

window.ThroneApp = angular.module('throne', ['BathroomsMod', 'ThroneConfig'])
    .config([function() {

    }])
    .run(['BathroomService', function(BathroomService) {

    }]);