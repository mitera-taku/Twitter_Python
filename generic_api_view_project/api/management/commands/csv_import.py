from django.core.management.base import BaseCommand
from pathlib import Path
from os.path import join
import csv
from django.contrib.auth.models import User
from api.models import Post, Comment

class Command(BaseCommand):
    def bulk_create_from_csv(self, model, csv_path, extra_fields=None):
        instances = []
        try:
            with open(csv_path, 'r', encoding='utf-8') as csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                    # デフォルトのフィールドを設定
                    if extra_fields:
                        row.update(extra_fields)

                    # モデルインスタンスを作成
                    instance = model(**row)
                    if model == User:
                        instance.set_password('12345678')
                    instances.append(instance)
            
            # 一括保存
            model.objects.bulk_create(instances)
            print(f"{len(instances)} records successfully created for {model.__name__}")
        except UnicodeDecodeError as e:
            self.stderr.write(f"Encoding error: {e}")

    def handle(self, *args, **options):
        current_dir_path = Path(__file__).resolve().parent
        csv_dir = join(current_dir_path, 'csvs')

        files_and_models = [
            ('users.csv', User, {'first_name': 'デフォルト名', 'last_name': 'デフォルト姓'}),
            ('posts.csv', Post, None),
            ('comments.csv', Comment, None),
        ]

        for file_name, model, extra_fields in files_and_models:
            csv_path = join(csv_dir, file_name)
            self.bulk_create_from_csv(model, csv_path, extra_fields)
