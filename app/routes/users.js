import Route from '@ember/routing/route';

export default Route.extend({
  model() {
    return this.get('store').findAll('user');
    // return [{"id": "4545", "info":"123"}];
  }
});
