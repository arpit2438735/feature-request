import featureRequestController from  "./featureRequestController";

let controller, FeatureRequestApiService, featureRequestListCallback,
    callback, $http, $rootScope, clientCallback, productCallback;
describe('featureRequestController', () => {
    beforeEach(inject((_$rootScope_) => {
        $rootScope = _$rootScope_;
        FeatureRequestApiService = {
            model: [],
            getFeatureRequestList: jasmine.createSpy('FeatureRequestApiService.getFeatureRequestList').and.callFake(() => {
                return {
                    then: function (cb) {
                        this.model = [{'title':'foo', 'description': 'bar'}];
                        featureRequestListCallback = cb;
                        return cb;
                    }
                };
            }),
        };

        $http = {
            get: jasmine.createSpy('$http.get').and.returnValue({then: angular.noop})
        };

        controller = new featureRequestController(FeatureRequestApiService, null, $http);
    }));

    it('should call FeatureRequestApiService.getFeatureRequestList', () => {
        expect(FeatureRequestApiService.getFeatureRequestList).toHaveBeenCalled();
    });

    it('should call get request for client', () => {
       expect($http.get).toHaveBeenCalledWith('/api/client/');
    });

    it('should call get request for product', () => {
       expect($http.get).toHaveBeenCalledWith('/api/product/');
    });

    describe('on call of client and product api\'s', () => {
        beforeEach(()=> {
            $http = {
                get(url) {
                    if (url === '/api/client/') {
                        return {
                            then: function (cb) {
                                clientCallback = cb;
                            }
                        }
                    }

                    if (url === '/api/product/') {
                        return {
                            then: function (cb) {
                                productCallback = cb;
                            }
                        }
                    }
                }
            };
            controller = new featureRequestController(FeatureRequestApiService, null, $http);

        });

        describe('and getting success response from client api', () =>{
            beforeEach(()=> {
                clientCallback({data: {clients:[{name: 'Client A', id: 1}, {name: 'Client B', id: 2}]}});
            });

            it('should add data in clientList scope', ()=> {
                expect(controller.clientList.length).toBe(2);
            });
        });

        describe('and getting success response from client api', () =>{
            beforeEach(()=> {
                productCallback({data: {products:[{name: 'Billing', id: 1}, {name: 'Policies', id: 2}]}});
            });

            it('should add data in clientList scope', ()=> {
                expect(controller.productList.length).toBe(2);
            });
        });
    });


});
