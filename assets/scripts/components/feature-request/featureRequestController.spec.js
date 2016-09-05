import featureRequestController from  "./featureRequestController";

let controller, FeatureRequestApiService, featureRequestListCallback,
    callback, $http, $rootScope, clientCallback, productCallback, modal;
describe('featureRequestController', () => {
    beforeEach(inject((_$rootScope_, $filter) => {
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
            addNewFeatureRequest: jasmine.createSpy('FeatureRequestApiService.addNewFeatureRequest').and.returnValue({then:angular.noop}),
            updateFeatureRequest: jasmine.createSpy('FeatureRequestApiService.updateFeatureRequest').and.returnValue({then:angular.noop})
        };

        $http = {
            get: jasmine.createSpy('$http.get').and.returnValue({then: angular.noop})
        };

        modal = {
            open: jasmine.createSpy('modal.open').and.returnValue({dismiss: jasmine.createSpy('modalInstane.dismiss')})
        };

        controller = new featureRequestController(FeatureRequestApiService, modal, $http, {}, $filter);
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

    describe('on click on new feature request', () => {
        beforeEach(() => {
            controller.openRequestFormModal();
        });

        it('should call open for modal', () => {
           expect(modal.open).toHaveBeenCalledWith({templateUrl: 'components/feature-request/new-feature-request.html', controllerAs: 'ctrl', scope: {}});
        });

        it('should not set featureRequest in controller', () => {
            expect(controller.featureRequest).toBeUndefined();
        });

        describe('on closing of modal', () => {
            beforeEach(()=>{
                controller.closeModal();
            });

            it('should call dimiss method of modal instance', ()=> {
                expect(controller.modalInstance.dismiss).toHaveBeenCalled();
            });
        });

        describe('on adding of new request from modal', ()=> {
            beforeEach(()=> {
                let form = {'$valid': true};
                controller.featureRequest = {
                    title: 'some',
                    target_date: new Date('2017','01','02')
                };
                controller.saveNewFeature(form);
            });

            it('should call addNewFeatureRequest for FeatureRequestApiService', ()=> {
               expect(FeatureRequestApiService.addNewFeatureRequest).toHaveBeenCalledWith({ title: 'some', target_date: '2017-02-02' });
            });

            it('should call dimiss method of modal instance', ()=> {
                expect(controller.modalInstance.dismiss).toHaveBeenCalled();
            });
        });
    });

    describe('on calling of openModelWithCurrentFeatureRequestValue', () => {

        beforeEach(() => {
            controller.clientModel = {'Client_C': {'id':1}, 'Client_A': {'id':2}};
            controller.productModel = {'Policies': {'id': 2}, 'Billing': {'id': 1}};
            controller.featureRequestList = [{
              "client_name": "Client_C",
              "client_priority": 1,
              "description": "Client wants to be able to send out a survey to evaluate customer satisfaction after issuing a new claim",
              "id": "9KVaD3BNYKN2Tsm6Sg2XKA",
              "product_area": "Policies",
              "target_date": "Fri, 11 Nov 2016 00:00:00 GMT",
              "title": "Add customer satisfaction survey"
            }];
            controller.openModelWithCurrentFeatureRequestValue(0);
        });

        it('should call open for modal', () => {
           expect(modal.open).toHaveBeenCalledWith({templateUrl: 'components/feature-request/new-feature-request.html', controllerAs: 'ctrl', scope: {}});
        });

        it('should set featureRequest in controller', () => {
            expect(controller.featureRequest.client_id).toBe(1);
            expect(controller.featureRequest.product_id).toBe(2);
            expect(controller.featureRequest.title).toBe('Add customer satisfaction survey');
        });

       describe('on updating new request from modal', ()=> {
            beforeEach(()=> {
                let form = {'$valid': true};
                controller.featureRequest = {
                    title: 'some',
                    target_date: new Date('2017','01','02')
                };
                controller.saveNewFeature(form, '123');
            });

            it('should call addNewFeatureRequest for FeatureRequestApiService', ()=> {
               expect(FeatureRequestApiService.updateFeatureRequest).toHaveBeenCalledWith('123', { title: 'some', target_date: '2017-02-02' });
            });

            it('should call dimiss method of modal instance', ()=> {
                expect(controller.modalInstance.dismiss).toHaveBeenCalled();
            });
        });
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
                expect(Object.keys(controller.clientModel).length).toBe(2);
            });
        });

        describe('and getting success response from client api', () =>{
            beforeEach(()=> {
                productCallback({data: {products:[{name: 'Billing', id: 1}, {name: 'Policies', id: 2}]}});
            });

            it('should add data in clientList scope', ()=> {
                expect(Object.keys(controller.productModel).length).toBe(2);
            });
        });
    });


});
