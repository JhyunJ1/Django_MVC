from django.db import models
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=128, verbose_name='상품명')
    price = models.IntegerField(verbose_name='가격')
    product_type = models.CharField(max_length=8, verbose_name='상품유형',
        choices=(
            ('단품', '단품'),
            ('세트', '세트'),
        )
    )

    tstamp = models.DateTimeField(auto_now_add=True, verbose_name='등록일시')

    class Meta:
        db_table = 'shinhan_product'
        verbose_name='상품'
        verbose_name_plural='상품'

# Create your models here.
class Comment(models.Model):
    member = models.ForeignKey('member.Member', on_delete=models.CASCADE, verbose_name='사용자')
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, verbose_name='상품')
    content = models.TextField(verbose_name='내용')

    tstamp = models.DateTimeField(auto_now_add=True, verbose_name="등록일시")

    class Meta:
        db_table = 'shinhan_product_comment'
        verbose_name = '상품 댓글'
        verbose_name_plural = '상품 댓글'

class Like(models.Model): # model 자체가 존재하면 좋아하는 상태 , 존재하지 않으면 좋아하지 않는 상태
    member = models.ForeignKey('member.Member', on_delete=models.CASCADE, verbose_name='사용자')
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, verbose_name='상품')

    class Meta:
        db_table = "shinhan_product_like"
        verbose_name = "상품 좋아요"
        verbose_name_plural = '상품 좋아요'   
