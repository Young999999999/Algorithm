const fs = require('fs');
const [hdr, ...body] = fs.readFileSync(0, 'utf8').trim().split('\n');
const [N, M, K] = hdr.split(' ').map(Number);

// 1) mapArr: N*M 크기의 Uint8Array (0 또는 1)
const mapArr = new Uint8Array(N * M);
for (let i = 0; i < N; i++) {
  const line = body[i];
  const base = i * M;
  for (let j = 0; j < M; j++) {
    // '1'.charCodeAt(0) === 49
    mapArr[base + j] = (line.charCodeAt(j) === 49) ? 1 : 0;
  }
}

// 2) minBreak: N*M 크기의 Uint8Array, 각 칸까지 부순 벽 최소 개수
const INF = K + 1;
const minBreak = new Uint8Array(N * M);
minBreak.fill(INF);
minBreak[0] = 0; // 시작점 (0,0)에선 0개 벽 부숨

// 3) queue: 최대 N*M*(K+1)개의 상태 저장용 Uint32Array
const maxStates = N * M * (K + 1);
const queue = new Uint32Array(maxStates);
let qs = 0, qe = 0;

// 상태 인코딩/디코딩
const encode = (r, c, b) => (((r * M + c) << 4) | b) >>> 0;
const decode = state => {
  const b = state & 0xF;
  const pos = state >>> 4;
  return [ (pos / M) | 0, pos % M, b ];
};

// BFS 초기화
queue[qe++] = encode(0, 0, 0);
let steps = 1;

// 4방향 벡터
const dirs = [1,0,  0,1,  -1,0,  0,-1];

while (qs < qe) {
  const levelSize = qe - qs;
  for (let i = 0; i < levelSize; i++) {
    const state = queue[qs++];
    const [r, c, b] = decode(state);

    // 도착 체크
    if (r === N - 1 && c === M - 1) {
      console.log(steps);
      process.exit(0);
    }

    // 인접 4칸
    for (let d = 0; d < 8; d += 2) {
      const nr = r + dirs[d];
      const nc = c + dirs[d+1];
      if (nr < 0 || nr >= N || nc < 0 || nc >= M) continue;

      const pos = nr * M + nc;
      const nb = b + mapArr[pos];
      if (nb > K || nb >= minBreak[pos]) continue;

      minBreak[pos] = nb;
      queue[qe++] = encode(nr, nc, nb);
    }
  }
  steps++;
}

console.log(-1);
