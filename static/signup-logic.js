var comparioApp = angular.module('comparioApp',[]);

comparioApp.controller('signUpController', ['$scope','$http'], function signUpController($scope, $http){
  username = $scope.username;
  password = $scope.password;
  confirmPassword = $scope.passwordConfirm;
  email = $scope.email;

  detailsObj = {username: username, password: password, confirmPassword: confirmPassword, email: email};
  detailsJSON = JSON.stringify(detailsObj);

  $http.post('/processSignUp', detailsJSON);
})
