K, G, M = list(map(int, input().split()))

#容量はGmlとMml

#それぞれの容器に入っている量
g_full = 0
m_full = 0


for i in range(K):
    if (g_full == G):
        g_full = 0
    elif (m_full == 0):
        m_full = M
    else:
        #グラスの空き容量
        g_rest = G - g_full
        #空き容量が十分だった時
        if (g_rest >= m_full):
            g_full += m_full
            m_full = 0
        #空き容量が足りなかった時
        else:
            m_full -= g_rest
            g_full = G

print(g_full, m_full)