#map = affine_map<(i, j) -> (i, j)>
module {
func.func @main() -> tensor<256x1024xf32> {
    %FC_INPUT = tensor.empty() : tensor<256x512xf32>
    %FC_WEIGHT = tensor.empty() : tensor<512x1024xf32>
    %c_init = arith.constant 0.0 : f32
    %matmul_init = tensor.splat %c_init : tensor<256x1024xf32>
    %FC_OUTPUT = linalg.matmul
                    ins(%FC_INPUT, %FC_WEIGHT : tensor<256x512xf32>, tensor<512x1024xf32>)
                    outs(%matmul_init : tensor<256x1024xf32>) -> tensor<256x1024xf32>
    %relu_init = tensor.empty() : tensor<256x1024xf32>
    %OUT = linalg.generic { indexing_maps = [#map],
                            iterator_types = ["parallel"]}
               ins(%FC_OUTPUT : tensor<256x1024xf32>)
               outs(%relu_init : tensor<128x1024xf32>) {
               ^bb0(%in: f32, %out: f32):
                    %c0 = arith.constant 0.0 : f32
                    %cmp = arith.cmpf ugt, %in, %c0 : f32
                    %sel = arith.select %cmp, %in, %c0 : f32
                    linalg.yield %sel : f32
               } -> tensor<128x1024xf32>
    func.return %OUT : tensor<128x1024xf32>
}
}
