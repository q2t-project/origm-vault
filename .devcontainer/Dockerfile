FROM python:3.11-slim

# 必要パッケージ
RUN apt-get update && apt-get install -y git curl && rm -rf /var/lib/apt/lists/*

# Python環境
RUN pip install --no-cache-dir pyyaml jupyter

# Obsidian連携系ファイル操作を支援
WORKDIR /workspace