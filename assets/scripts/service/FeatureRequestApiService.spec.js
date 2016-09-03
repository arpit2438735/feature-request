import FeatureRequestApiService from "./FeatureRequestApiService";

let service, $http, $rootScope, featureRequestListCallback, newfeatureRequestCallback;

describe('FeatureRequestService', () => {
    beforeEach(()=> {
        $http = {
            get: jasmine.createSpy('$http.get').and.callFake(() => {
                return {
                    then: function (cb) {
                        featureRequestListCallback = cb;
                    }
                };
            }),
            post: jasmine.createSpy('$http.post').and.callFake(() => {
                return {
                    then: function (cb) {
                        newfeatureRequestCallback = cb;
                    }
                };
            })
        };
    });

    beforeEach(() => {
        service = new FeatureRequestApiService($http);
    });

    it('should intialize its model with empty list', () => {
       expect(service.model.length).toBe(0);
    });

    describe('on calling of getFeatureRequestList', function () {
        beforeEach(() => {
            service.getFeatureRequestList();
        });

        it('should call $http.get', () => {
            expect($http.get).toHaveBeenCalledWith('/api/feature-request/');
        });

        describe('on get list of feature list from backend', () => {
            beforeEach(() => {
                featureRequestListCallback([{'title': 'foo', 'description': 'bar'}]);
            });

            it('should add value in the same model', () => {
               expect(service.model.length).toBe(1);
            });
        });
    });

    describe('on calling of getFeatureRequestList', function () {
            const newFeautreRequest = {'title': 'newfoo', 'description': 'newbar'};
            beforeEach(() => {
                service.addNewFeatureRequest(newFeautreRequest);
            });

            it('should call $http.post', () => {
                expect($http.post).toHaveBeenCalledWith('/api/feature-request/', newFeautreRequest);
            });

            describe('on get list of feature list from backend', () => {
                beforeEach(() => {
                    newfeatureRequestCallback(newFeautreRequest);
                });

                it('should add value in the same model', () => {
                   expect(service.model.length).toBe(1);
                });
            });
    });
});