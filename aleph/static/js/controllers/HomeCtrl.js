import aleph from '../aleph';

aleph.controller('HomeCtrl', ['$scope', '$location', '$route', 'Collection', 'collections', 'CountryCodes', 'Authz', 'Role', 'Title', 'statistics', 'metadata',
    function($scope, $location, $route, Collection, collections, CountryCodes, Authz, Role, Title, statistics, metadata) {

  $scope.statistics = statistics;
  $scope.session = metadata.session;
  $scope.metadata = metadata;
  $scope.entitiesQuery = {q: ''};
  $scope.documentsQuery = {q: ''};
  $scope.authz = Authz;
  $scope.collectionData = [];

  Title.set("Welcome");

  $scope.searchDocuments = function(form) {
    $location.path('/documents');
    $location.search({q: $scope.documentsQuery.q});
  };

  $scope.searchEntities = function(form) {
    $location.path('/entities');
    $location.search({q: $scope.entitiesQuery.q});
  };

  $scope.createCollection = function($event) {
    Collection.create().then(function(coll) {
      $location.path('/collections/' + coll.id);
    });
  };

  var getCollectionId = function() {
      CountryCodes.get().then(function(codes) {
          angular.forEach(collections.result.results, function (collection) {
              if (collection.public) {
                  var country_code = collection.foreign_id.split('_')[0].toUpperCase();
                  var check = Object.keys(codes).indexOf(country_code) !== -1;
                  $scope.collectionData.push({
                      'country': check ? codes[country_code].toLowerCase() : 'nf',
                      'url': '/documents?filter:collection_id=' + collection.id,
                      'country_code': country_code.toLowerCase()
                  })
              }
          });
      });

  };
  getCollectionId();
}]);
