class featureRequestController {
    constructor(FeatureRequestApiService) {
        FeatureRequestApiService.getFeatureRequestList().then(() => {
            this.featureRequestList = FeatureRequestApiService.model;
        });
    }
}

featureRequestController.$inject = ['FeatureRequestApiService'];

export default featureRequestController;