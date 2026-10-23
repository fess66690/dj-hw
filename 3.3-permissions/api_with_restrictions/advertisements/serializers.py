from django.contrib.auth.models import User
from rest_framework import serializers

from advertisements.models import Advertisement, AdvertisementStatusChoices


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at', )

    def create(self, validated_data):
        """Метод для создания"""

        # Простановка значения поля создатель по-умолчанию.
        # Текущий пользователь является создателем объявления
        # изменить или переопределить его через API нельзя.
        # обратите внимание на `context` – он выставляется автоматически
        # через методы ViewSet.
        # само поле при этом объявляется как `read_only=True`
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        """Метод для валидации. Вызывается при создании и обновлении."""

        request = self.context.get("request")
        if request and request.user.is_authenticated:
            # Определяем статус: новый или обновляемый
            if self.instance:
                # Обновление — проверяем, не меняется ли статус на OPEN
                old_status = self.instance.status
                new_status = data.get("status", old_status)
                if new_status == AdvertisementStatusChoices.OPEN:
                    # Считаем только если раньше не было OPEN
                    if old_status != AdvertisementStatusChoices.OPEN:
                        count = request.user.advertisement_set.filter(
                            status=AdvertisementStatusChoices.OPEN
                        ).count()
                        if count >= 10:
                            raise serializers.ValidationError(
                                "Не более 10 открытых объявлений."
                            )
            else:
                # Создание — проверяем количество открытых объявлений
                count = request.user.advertisement_set.filter(
                    status=AdvertisementStatusChoices.OPEN
                ).count()
                # Если в данных указан OPEN или по умолчанию OPEN
                status = data.get("status", AdvertisementStatusChoices.OPEN)
                if status == AdvertisementStatusChoices.OPEN and count >= 10:
                    raise serializers.ValidationError(
                        "Не более 10 открытых объявлений."
                    )

        return data
