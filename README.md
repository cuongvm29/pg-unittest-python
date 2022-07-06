## Mục lục
* [1. Khái niệm về Unit Test](#1-khái-niệm-về-unit-test)
* [2. Thiết kế Unit test](#2-thiết-kế-unit-test)  
* [3. Ứng dụng Unit test](#3-ứng-dụng-unit-test)  
* [4. Lợi ích của việc áp dụng Unit test](#4-lợi-ích-của-việc-áp-dụng-unit-test)
* [5. Unittest trong python](##5-unittest-trong-python)


## 1. Khái niệm về Unit Test 
Unit Test là gì?

Unit Test là một loại kiểm thử phần mềm trong đó các đơn vị hay thành phần riêng lẻ của phần mềm được kiểm thử. Kiểm thử đơn vị được thực hiện trong quá trình phát triển ứng dụng. Mục tiêu của Kiểm thử đơn vị là cô lập một Unit là gì?

Một Unit là một thành phần PM nhỏ nhất mà ta có thể kiểm tra được như các hàm (Function), thủ tục (Procedure), lớp (Class), hoặc các phương thức (Method).

Vì Unit được chọn để kiểm tra thường có kích thước nhỏ và chức năng hoạt động đơn giản, chúng ta không khó khăn gì trong việc tổ chức, kiểm tra, ghi nhận và phân tích kết quả kiểm tra nên việc phát hiện lỗi sẽ dễ dàng xác định nguyên nhân và khắc phục cũng tương đối dễ dàng vì chỉ khoanh vùng trong một Unit đang kiểm tra.

Mỗi UT sẽ gửi đi một thông điệp và kiểm tra câu trả lời nhận được đúng hay không, bao gồm:
    - Các kết quả trả về mong muốn
    - Các lỗi ngoại lệ mong muốn

Các đoạn mã UT hoạt động liên tục hoặc định kỳ để thăm dò và phát hiện các lỗi kỹ thuật trong suốt quá trình phát triển, do đó UT còn được gọi là kỹ thuật kiểm nghiệm tự động. UT có các đặc điểm sau:
    - Đóng vai trò như những người sử dụng đầu tiên của hệ thống.
    - Chỉ có giá trị khi chúng có thể phát hiện các vấn đề tiềm ẩn hoặc lỗi kỹ thuật.


## 2. Thiết kế Unit test

Mỗi UT đều được tiết kế theo trình tự sau:
    - Thiết lập các điều kiện cần thiết: khởi tạo các đối tượng, xác định tài nguyên cần thiết, xây dựng các dữ liệu giả…
    - Triệu gọi các phương thức cần kiểm tra.
    - Kiểm tra sự hoạt động đúng đắn của các phương thức.
    - Dọn dẹp tài nguyên sau khi kết thúc kiểm tra.

## 3. Ứng dụng Unit test
    - Kiểm tra mọi đơn vị nhỏ nhất là các thuộc tính, sự kiện, thủ tục và hàm.
    - Kiểm tra các trạng thái và ràng buộc của đối tượng ở các mức sâu hơn mà thông thường chúng ta không thể truy cập được.
    - Kiểm tra các quy trình (process) và mở rộng hơn là các khung làm việc(workflow – tập hợp của nhiều quy trình)

## 4. Lợi ích của việc áp dụng Unit test
Thời gian đầu, người ta thường do dự khi phải viết UT thay vì tập trung vào code cho các chức năng nghiệp vụ. Công việc viết Unit Test có thể mất nhiều thời gian hơn code rất nhiều nhưng lại có lợi ích sau:
    - Tạo ra môi trường lý tưởng để kiểm tra bất kỳ đoạn code nào, có khả năng thăm dò và phát hiện lỗi chính xác, duy trì sự ổn định của toàn bộ PM và giúp tiết kiệm thời gian so với công việc gỡ rối truyền thống.
    - Phát hiện các thuật toán thực thi không hiệu quả, các thủ tục chạy vượt quá giới hạn thời gian.
    - Phát hiện các vấn đề về thiết kế, xử lý hệ thống, thậm chí các mô hình thiết kế.
    - Phát hiện các lỗi nghiêm trọng có thể xảy ra trong những tình huống rất hẹp.
    Tạo hàng rào an toàn cho các khối mã: Bất kỳ sự thay đổi nào cũng có thể tác động đến hàng rào này và thông báo những nguy hiểm tiềm tàng.

Trong môi trường làm việc Unit Test còn có tác dụng rất lớn đến năng suất làm việc:
    - Giải phóng chuyên viên QA khỏi các công việc kiểm tra phức tạp.
    - Tăng sự tự tin khi hoàn thành một công việc. Chúng ta thường có cảm giác không chắc chắn về các đoạn mã của mình như liệu các lỗi có quay lại không, hoạt động của module hiện hành có bị tác động không, hoặc liệu công việc hiệu chỉnh mã có gây hư hỏng đâu đó…
    - Là công cụ đánh giá năng lực của bạn. Số lượng các tình huống kiểm tra (test case) chuyển trạng thái “pass” sẽ thể hiện tốc độ làm việc, năng suất của bạn.

## 5.Unittest trong python:
1. Cài thư viện
    ```
        pip install -U pytest
    ```
2. Kiểm tra thư viện
    ```
        pytest --version
    ```
3. Ví dụ
    * Tạo file test_sample.py 
        ```py
            # content of test_sample.py
            def func(x):
                return x + 1


            def test_answer():
                assert func(4) == 5
        ```
    * Chạy command
        ```
            pytest test_sample.py 
        ```
    * Hiển thị coverage in console
        ```
            pytest test_sample.py --cov  
        ```
    * Tạo file coverage.html
        ```
            pytest test_sample.py --cov  --cov-report=html
        ``` 
4. Một số khái niệm cần tìm hiểu:
    * Mock (return_value, side_effect)
    * Input
    * Exepct
    * Coverage

5. Docs
    - https://docs.pytest.org/en/7.1.x/getting-started.html