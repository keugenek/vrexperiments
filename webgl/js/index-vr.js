import ForceGraphVR from '3d-force-graph-vr';
const Graph = ForceGraphVR()
  (document.getElementById('3d-graph'))
  .jsonUrl('datasets/flow-modules.json')
    .nodeLabel('name')
    .nodeAutoColorBy('group');