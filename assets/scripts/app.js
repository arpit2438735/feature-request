import angular from 'angular';
import uiBootstrap from 'angular-ui-bootstrap';

import component from './components/feature-request/feature-request';

angular.module('feature-request', [uiBootstrap, component]);

export default 'featureRequest';