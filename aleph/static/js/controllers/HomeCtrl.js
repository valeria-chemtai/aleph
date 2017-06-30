import aleph from '../aleph';

aleph.controller('HomeCtrl', ['$scope', '$location', '$route', 'Collection', 'Articles', 'Authz', 'Role', 'Title', 'statistics', 'metadata',
    function($scope, $location, $route, Collection, Articles, Authz, Role,
    Title, statistics, metadata) {

  $scope.statistics = statistics;
  $scope.session = metadata.session;
  $scope.metadata = metadata;
  $scope.entitiesQuery = {q: ''};
  $scope.documentsQuery = {q: ''};
  $scope.authz = Authz;
  $scope.articles = [];

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

  var loadArticles = function() {
      Articles.get().then(function(data) {
        console.log("data: ", data);
        console.log("data entry: ", data.entry);
        $scope.articles = data.entry;
      });

  };

  loadArticles();

}]);
