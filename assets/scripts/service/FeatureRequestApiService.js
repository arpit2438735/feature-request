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
               this._model.push(response);
            });
    }

    get model() {
        return this._model;
    }
}

FeatureRequestApiService.$inject = ['$http'];

export default FeatureRequestApiService;