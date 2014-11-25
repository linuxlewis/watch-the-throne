angular.module('BathroomsMod').factory('BathroomModel', ['bathroomPicRoot', function(picRoot) {
    function Bathroom(data) {
        this.id = data.id;
        this.deviceId = data.device;
        this.name = data.name;
        this.picture = data.picture.match('\/static\/.*$')[0];
        this.available = data.available;
    };

    return Bathroom;
}]);