import featureRequestController from  "./featureRequestController";

let controller, FeatureRequestApiService, featureRequestListCallback;
describe('featureRequestController', () => {
    beforeEach(() => {
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
        controller = new featureRequestController(FeatureRequestApiService);
    });

    it('should call FeatureRequestApiService.getFeatureRequestList', () => {
        expect(FeatureRequestApiService.getFeatureRequestList).toHaveBeenCalled();
    });
});
