import angular from "angular";

let $http;

class FeatureRequestApiService {
    constructor(_$http_) {
        this.$http = _$http_;
        this._model = [];
    }

    getFeatureRequestList() {
        this.model.length = 0;
        return this.$http.get('/api/feature-request/').then((response) =>{
                this._model.push.apply(this._model, response.data.feature_requests);
            });
    }

    addNewFeatureRequest(data) {
        return this.$http.post('/api/feature-request/', data).then((response) => {
               this._model.push(response.data.feature_request);
            });
    }

    updateFeatureRequest(featureId, updateRequest) {
        return this.$http.put('/api/feature-request/'+ featureId, updateRequest).then((response) => {
                this.model.forEach((feature, index) => {
                    if(feature.id === featureId) {
                        this.model[index] = response.data.feature_request;
                        return;
                    }
                });
            });
    }

    get model() {
        return this._model;
    }
}

FeatureRequestApiService.$inject = ['$http'];

export default FeatureRequestApiService;