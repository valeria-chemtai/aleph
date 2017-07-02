import aleph from '../aleph';

aleph.factory('CountryCodes', ['$q', '$http', '$location', 'Metadata',
    function($q, $http, $location, Metadata) {

  var getCountryCodes = function() {
    var dfd = $q.defer();
    $http.get('static/assets/country_codes.json').then(function(res) {
      dfd.resolve(res.data);
    }, function(err) {
      dfd.reject(err);
    });
    return dfd.promise;
  };

  return {
    get: getCountryCodes
  };
}]);
