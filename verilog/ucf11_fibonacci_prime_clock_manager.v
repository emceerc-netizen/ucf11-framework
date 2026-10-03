module ucf11_fibonacci_prime_clock_manager (
    input wire clk,
    input wire reset,
    output reg pulse
);

    reg [15:0] fib_a;
    reg [15:0] fib_b;
    reg [15:0] count;

    initial begin
        fib_a <= 16'd1;
        fib_b <= 16'd1;
        count <= 16'd0;
        pulse <= 1'b0;
    end

    always @(posedge clk or posedge reset) begin
        if (reset) begin
            fib_a <= 16'd1;
            fib_b <= 16'd1;
            count <= 16'd0;
            pulse <= 1'b0;
        end else begin
            count <= count + 1;
            if (count[0] == 1'b1) begin
                pulse <= 1'b1;
            end else begin
                pulse <= 1'b0;
            end

            if (count % 3 == 0) begin
                {fib_a, fib_b} <= {fib_b, fib_a + fib_b};
            end
        end
    end

endmodule
