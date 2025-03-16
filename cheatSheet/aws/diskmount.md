## aws EBS 마운트과정

- 볼륨 추가 과정 생략



하위 aws 명령어

```bash
lsblk # 전체 디스크확인
sudo mkfs -t xfs /dev/{disk} # xfs 타입 포맷 ext4 포맷 확인후 타입포맷 사용
sudo mount /dev/{disk} /mnt  # 디스크를 /mnt 폴더에 마운트
sudo umount /mnt # 디스크를 언마운트 
# 이외 df -Th 커멘드를 통해 마운트 여부확인

```