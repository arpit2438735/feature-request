import FeatureRequestApiService from "./FeatureRequestApiService";

let service, $http, $rootScope, featureRequestListCallback, newfeatureRequestCallback, updateFeatureRequestCallback;

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
            }),
            put: jasmine.createSpy('$http.put').and.callFake(() => {
                return {
                    then: function (cb) {
                        updateFeatureRequestCallback = cb;
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

    describe('on calling of getFeatureRequestList', () => {
        beforeEach(() => {
            service.getFeatureRequestList();
        });

        it('should call $http.get', () => {
            expect($http.get).toHaveBeenCalledWith('/api/feature-request/');
        });

        describe('on get list of feature list from backend', () => {
            beforeEach(() => {
                featureRequestListCallback({'data': {'feature_requests': [{'title': 'foo', 'description': 'bar'}]}});
            });

            it('should add value in the same model', () => {
               expect(service.model.length).toBe(1);
            });
        });
    });

    describe('on calling of getFeatureRequestList', () => {
            const newFeautreRequest = {data: {feature_request: {'title': 'newfoo', 'description': 'newbar'}}};
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

    describe('on send put request with updated value', () => {
        let updateData = {'id': 2, 'title': 'test', 'description': 'testing'};

        beforeEach(() => {
            service.getFeatureRequestList();
            featureRequestListCallback({'data': {'feature_requests': [{'id': 1,'title': 'foo', 'description': 'bar'},
                                                                {'id': 2, 'title': 'foos', 'description': 'bars'}]}});
            service.updateFeatureRequest(2, updateData);
        });

        it('should call $http.post', () => {
            expect($http.put).toHaveBeenCalledWith('/api/feature-request/2', updateData);
        });

        describe('on getting success response', ()=> {
            beforeEach(()=> {
                updateFeatureRequestCallback({'data': {'feature_request': updateData}});
            });

            it('should update the value of second indexed model', () => {
                expect(service.model[1].title).toBe(updateData.title);
                expect(service.model[1].description).toBe(updateData.description);
            });
        });
    });
});