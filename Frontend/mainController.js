var app = angular.module('myApp', []);

app.controller('myCtrl', function($scope, $http) { 
    
    //check connection
    $scope.init = function(){
        $scope.show2 = false;
        $http({
            method: "GET",
            dataType: 'JSONP', 
            url: "http://localhost:5000/"
        }).then(function(data){
            $scope.connected = "ALL DAY LONG KURWA";
            $scope.show2 = true;
        }, function(error){
            $scope.connected = "Missing connection. Please refresh or restart flask server.";
            $scope.sho2 = false;
        });
    }
    
    //get data
    $scope.getData = function(){
        $scope.show = false;
        $scope.show1 = false;
        if($scope.surname||$scope.name){
            $http({
                method: "GET",
                dataType: 'JSONP',
                url: "http://localhost:5000/user?surname=" + $scope.surname+"&name="+$scope.name
            }).then(function(data){
                if(data.data['id']==='None'){
                    $scope.show1 = true;
                }else{
                    $scope.dane = data.data;
                    $scope.pubs = $scope.dane['publications'];
                }                
            }, function(error){
                console.log(error);
                alert("Something gones wrong");
            })
        }else{
            $scope.show = true;
        }
        
    }
});