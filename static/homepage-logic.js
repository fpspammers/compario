var comparioApp = angular.module('comparioApp',[]);

comparioApp.controller('searchController',['$scope','$http', function($scope,$http){

  $scope.searchProduct = function searchProduct(){

    console.log("Submitted");
    console.log($scope.searchBar);
    var searchString = $scope.searchBar;

    $http({
      method: 'POST',
      url: '/searchProcess',
      data: {'searchBar': searchString}
      }).then(
        function(response){
          console.log("Success");
        },
        function(){
          console.log("Failure");
        }
      );
  }
}]);
